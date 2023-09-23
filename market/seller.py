from flask import Blueprint,render_template,request,flash,redirect,url_for
from .decorator import login_required
from flask_login import current_user
import cloudinary.uploader

sellers = Blueprint('sellers', __name__)

@sellers.route('/seller-home', methods=['GET'])
@login_required('seller')
def seller_home():
    
    
    return render_template('Seller/seller_page.html',user = current_user)

@sellers.route('/seller-dashboard', methods =['GET'])
@login_required('seller')
def seller_dashboard():
    
    
    return render_template('Seller/seller-dashboard.html', user = current_user)

@sellers.route('/upload', methods=['POST'])
@login_required('seller')
def upload_product():
    try:
        uploaded_image = request.files['product-img']

        if uploaded_image:
            category = request.form['product-categories']

            result = cloudinary.uploader.upload(
                uploaded_image,
                folder=f'product-images/{category}',  
            )

            product_name = request.form.get('product-name')
            product_price = request.form.get('product-price')
            product_description = request.form.get('product-description')

            flash(f'Product uploaded successfully! Image URL: {result["secure_url"]}', category='success')

            return redirect(url_for('sellers.seller_home'))  

        else:
            flash('No image file provided.', category='error')
            return redirect(url_for('sellers.seller_home'))  
            

    except Exception as e:
        flash(f'Error uploading product: {str(e)}', category='error')
        return redirect(url_for('sellers.seller_home'))  
      