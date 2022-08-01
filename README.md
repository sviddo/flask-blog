# Flask blog

This application acts as a blog where you can handle your posts and view other ones. Here is functionality implemented:
- Authentication (register/log in/log out)
- Manage your profile: update profile picture and info
- Create/update/delete own posts and view other ones

<h3>Try it out:</h3>

```
git clone https://github.com/sviddo/flask-blog.git
cd flask-blog
docker build -t flask-app .
docker run -p 5000:80 flask-app
```

Then in browser go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
