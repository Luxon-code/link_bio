import reflex as rx
from link_bio.components.link_button import link_button
def links() -> rx.component:
    return rx.vstack(
        link_button("Tiwtch","https://www.twitch.tv"),
        link_button("Facebook","https://www.facebook.com"),
        link_button("Twitter","https://twitter.com"),
        link_button("YouTube","https://www.youtube.com"),
        width="100%",
    )