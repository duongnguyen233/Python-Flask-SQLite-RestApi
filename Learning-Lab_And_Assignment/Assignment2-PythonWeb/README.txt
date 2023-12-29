Url for API: (GET list of blogs)
http://127.0.0.1:5000/listBlog


// ---------------------Issues-------------------------
Trong lúc hoàn thành bài tập, mình có gặp phải một số lỗi. Mặc dù đã tìm kiếm trên mạng và fix được nhưng mình cũng không hiểu rõ lắm.

// --- Issue 1
Phải add thêm app.app_context().push() sau khi tạo database và khởi tạo bằng tay.
db = SQLAlchemy(app)
app.app_context().push()
Khởi tạo database bằng tay (Để sinh ra file data.sqlite):
python
from controller import db
db.create_all()
quit()

// --- Issue 2
Trong lúc chạy sẽ có lỗi ImportError: cannot import name 'Mapping' from 'collections'
Theo mình tìm hiểu là thư viện collections được thay thế bằng collections.abc từ python 3.0
-> Mình vào thay 2 files trong thư viện flask từ collections sang collections.abc thì chạy được
