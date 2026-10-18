# %%
import datetime as dt
import os

import numpy as np
import pydicom as dcm


class Video:
    def __init__(self, dataset: dcm.FileDataset):
        self.dataset = dataset

    @property
    def data(self) -> np.ndarray:
        """
        Returns:
            np.ndarray: Video data indexed as `(frame, row, column)`.
        """
        return self.dataset.pixel_array

    @property
    def frames(self) -> int:
        """
        Returns:
            int: Number of frames.
        """
        return self.dataset.pixel_array.shape[0]

    @property
    def rows(self) -> int:
        """
        Returns:
            int: Number of rows per frame.
        """
        return self.dataset.pixel_array.shape[1]

    @property
    def cols(self) -> int:
        """
        Returns:
            int: Number of columns per frame.
        """
        return self.dataset.pixel_array.shape[2]

    @property
    def datetime(self) -> dt.datetime:
        date = self.dataset["ContentDate"].value
        time = self.dataset["ContentTime"].value
        tz = self.dataset["TimezoneOffsetFromUTC"].value
        return dt.datetime.strptime(f"{date}T{time}Z{tz}", "%Y%m%dT%H%M%SZ%z")


def load(path: os.PathLike) -> Video:
    dataset = dcm.dcmread(path)
    return Video(dataset)
