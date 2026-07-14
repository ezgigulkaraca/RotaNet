import streamlit as st


def section_title(title: str) -> None:
    """
    Display a section title.
    """
    st.markdown(f"## {title}")


def info_message(message: str) -> None:
    """
    Display an informational message.
    """
    st.info(message)


def success_message(message: str) -> None:
    """
    Display a success message.
    """
    st.success(message)


def error_message(message: str) -> None:
    """
    Display an error message.
    """
    st.error(message)


def horizontal_divider() -> None:
    """
    Display a horizontal divider.
    """
    st.divider()


def empty_placeholder(title: str, message: str) -> None:
    """
    Display a placeholder box for features
    that are not implemented yet.
    """

    with st.container(border=True):

        st.subheader(title)

        st.caption(message)
