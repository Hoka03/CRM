JAZZMIN_SETTINGS = {
    "site_title": "My Admin",
    "site_header": "My Administration",
    "welcome_sign": "Welcome to My Admin",
    "show_ui_builder": True,  # Enables the UI builder for customizing the theme
    "user_avatar": "myapp.CustomUser.avatar_url",  # Example of setting a custom avatar field
    "top_menu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "auth"},
        {"app": "myapp"},
    ],
    "user_menu_links": [
        {"name": "Support", "url": "https://support.example.com", "new_window": True},
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "related_modal_active": True,  # Enables related modals in the admin
    "theme": "dark",
    "custom_css": "css/my_custom_admin.css",  # Path to custom CSS file
    "custom_js": "js/my_custom_admin.js",  # Path to custom JS file
}
