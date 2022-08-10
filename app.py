"""Main function for the frame navigator application, Developed using Streamlit library."""

import os

import streamlit as st

from video_streamer import video_streaming


class StreamlitAppUI:
    """Streamlit application user inference."""

    def __init__(self):
        st.set_page_config(page_title='Video Streamer', layout='wide')
        self.ui_created = True
        self.task_mode = None
        self.data_path = ''
        self.data_path_dict = {'Video': 'https://www.youtube.com/watch?v=nP-nMZpLM1A',
                               'WebCam_Video': ''}
        self.setup_ui()

    def setup_ui(self):
        """Set main UI for task selection."""
        self.task_mode = st.sidebar.selectbox('Task', ['Video', 'WebCam_Video'])

        data_path = self.data_path_dict[self.task_mode]
        self.data_path = data_path
        if self.task_mode == 'Video':
            self.data_path = st.sidebar.text_input('Data Path', data_path)
            if not self.data_path.startswith('https://') and not os.path.exists(self.data_path):
                st.write(f'{self.data_path} path does not exists!')
                self.ui_created = False
                return
            if self.data_path.startswith('https://'):
                st.video(self.data_path, format="video/mp4")
                self.ui_created = False
                return

        self.ui_created = True


def main():
    """Streamlit app video streaming."""
    app_ui = StreamlitAppUI()
    if not app_ui.ui_created:
        return

    video_streaming(app_ui)


if __name__ == '__main__':
    main()
