import env_setup
env_setup.setup()
from env_setup import on_production_server
from webapp2 import Route, WSGIApplication


application = WSGIApplication(
    [
        # main screen

        # warmup
        Route(r'/_ah/warmup',
              handler='handlers.warmup.WarmupHandler',
              name='warmup',
              ),
        # make client
        Route(r'/test',
              handler='handlers.main.MainHandler',
              name='main',
              ),
        Route(r'/make_post',
              handler='handlers.main.AllPostsHandler',
              name='make_posts',
              ),
        Route(r'/get_single_post',
              handler='handlers.main.SinglePostsHandler',
              name='get_single_post',
              ),
        Route(r'/is_logged_in',
              handler='handlers.main.IsLoggedInHandler',
              name='IsLoggedInHandler',
              ),
         Route(r'/login',
              handler='handlers.main.LoginHandler',
              name='login_handler',
              ),
        Route(r'/create_posts',
              handler='handlers.main.CreatePostsHandler',
              name='CreatePostsHandler',
              ),
        Route(r'/your_posts',
              handler='handlers.main.YourPostsHandler',
              name='YourPostsHandler',
              ),
        Route(r'/update_post',
              handler='handlers.main.UpdatePostsHandler',
              name='UpdatePostsHandler',
              ),


    ],
    debug=not on_production_server
)
