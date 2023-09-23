from  flask import Blueprint,render_template
from flask_login import login_required
from  .decorator import admin_required

admin_panel = Blueprint('admin_panel', __name__)

@admin_panel.route('/admin',methods=['GET'])
@admin_required
@login_required
def admin():
    
    return render_template('Admin/admin.html')
