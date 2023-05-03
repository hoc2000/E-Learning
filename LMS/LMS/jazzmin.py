JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Library Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "CoursePM",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "CoursePM",

    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to course management",

    # Copyright on the footer
    "copyright": "CoursePM ANSV",



    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index",
            "permissions": ["auth.view_user"]},



        # model admin to link to (Permissions checked against model)
        {"model": "app.Course"},

    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": ["app.Lesson", "app.Video"],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "app"],

    # Custom links to append to app groups, keyed on app name
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "app.Author": "fas fa-chalkboard-teacher",
        "app.Categories": "fas fa-layer-group",
        "app.Comment": "fas fa-comment",
        "app.Course": "fas fa-book",
    },
    "related_modal_active": False,

    "changeform_format": "single",
}
