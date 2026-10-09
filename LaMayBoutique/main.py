from eapp import app, db
import eapp.index
import eapp.admin

if __name__ == '__main__':
    # Tự động map code models.py thành bảng trong MySQL
    with app.app_context():
        db.create_all()

    app.run(debug=True)