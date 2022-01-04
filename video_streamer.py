"""Streamlit video processing functions."""

from abc import ABC

import av
from aiortc.contrib.media import MediaPlayer
from streamlit_webrtc import RTCConfiguration, WebRtcMode, webrtc_streamer, VideoProcessorBase


def video_streaming(app_ui):
    """Video streaming and web camera streaming."""
    media_file_info = {"file_path": app_ui.data_path, "video": True, "audio": True}

    def create_player():
        """Create webrtc_ctx media player."""
        return MediaPlayer(str(media_file_info["file_path"]))

    class VideoProcessor(VideoProcessorBase, ABC):
        """Video streamer and webcam video streamer."""

        def __init__(self):
            self.frame_count = 0

        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            """Return video frames recursively from media player."""
            frame = frame.to_ndarray(format="bgr24")
            self.frame_count += 1
            # TODO: process the frame
            return av.VideoFrame.from_ndarray(frame, format="bgr24")

    def get_webrtc_ctx():
        """Return webrtc_ctx media player."""
        rtc_configuration = RTCConfiguration(
            iceServers=[{"urls": ["stun:stun.l.google.com:19302"]}]
        )
        if app_ui.task_mode in ["WebCam_Video"]:
            _webrtc_ctx = webrtc_streamer(key="video", rtc_configuration=rtc_configuration,
                                          video_processor_factory=VideoProcessor,
                                          async_processing=False,
                                          media_stream_constraints={"audio": True, "video": True})
        elif app_ui.task_mode in ["Video"]:
            _webrtc_ctx = webrtc_streamer(
                key=f"media-streaming-{media_file_info['file_path']}", mode=WebRtcMode.RECVONLY,
                rtc_configuration=rtc_configuration,
                media_stream_constraints={"video": media_file_info["video"],
                                          "audio": media_file_info["audio"], },
                player_factory=create_player, video_processor_factory=VideoProcessor,
            )
        else:
            _webrtc_ctx = None
        return _webrtc_ctx

    webrtc_ctx = get_webrtc_ctx()
    if webrtc_ctx is not None and webrtc_ctx.state.playing:
        # NOTE: The video transformation with some process and loop displaying the result labels
        # here are running in different threads asynchronously.
        # Then the rendered video frames and the label displayed here are not strictly synchronized.
        # TODO: perform some process or show some results based on frame processing.

        # uncomment next line see asynchronous results.
        # print(webrtc_ctx.video_processor.frame_count)
        pass
