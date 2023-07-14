# flake8: noqa
import math
from pbrenko_trials.domain.brick import Brick
from pbrenko_trials.domain.pbrenko import PBRenko


class PBRenkoCreator:
    def __init__(self):
        self.data = []
        self.bricks = []
        self.low_wick = 0
        self.high_wick = 0
        self.number_of_leaks = 0
    
    def create_pbrenko(self, data, percent):
        self.data = data
        self.percent = percent

        if len(self.data) == 0:
            return []

        gap = float(self.data[0]) * self.percent / 100
        for i, d in enumerate(self.data):
            if i == 0:
                if len(self.bricks) == 0:
                    self.bricks.append(Brick(type="first", open=float(d), close=float(d), high=float(d), low=float(d)))
            else:
                if self.bricks[-1].type == "up":
                    if d > self.bricks[-1].close:
                        delta = d - self.bricks[-1].close
                        fcount = math.floor(delta / gap)
                        if fcount != 0:
                            if self.low_wick == 0:
                                self.add_bricks("up", fcount, gap)
                            else:
                                self.add_bricks("up", fcount, gap, self.low_wick)
                            gap = d * self.percent / 100
                            self.low_wick = 0
                            self.high_wick = 0
                        else:
                            if d > self.high_wick:
                                self.high_wick = d
                    elif d < self.bricks[-1].open:
                        delta = self.bricks[-1].open - d
                        fcount = math.floor(delta / gap)
                        if fcount != 0:
                            if self.high_wick == 0:
                                self.add_bricks("down", fcount, gap)
                            else:
                                self.add_bricks("down", fcount, gap, self.high_wick)
                            gap = d * self.percent / 100
                            self.high_wick = 0
                            self.low_wick = 0
                        else:
                            if self.low_wick == 0 or d < self.low_wick:
                                self.low_wick = d
                elif self.bricks[-1].type == "down":
                    if d < self.bricks[-1].close:
                        delta = self.bricks[-1].close - d
                        fcount = math.floor(delta / gap)
                        if fcount != 0:
                            if self.high_wick == 0:
                                self.add_bricks("down", fcount, gap)
                            else:
                                self.add_bricks("down", fcount, gap, self.high_wick)
                            self.high_wick = 0
                            self.low_wick = 0
                            gap = d * self.percent / 100
                        else:
                            if self.low_wick == 0 or d < self.low_wick:
                                self.low_wick = d
                    elif d > self.bricks[-1].open:
                        delta = d - self.bricks[-1].open
                        fcount = math.floor(delta / gap)
                        if fcount != 0:
                            if self.low_wick == 0:
                                self.add_bricks("up", fcount, gap)
                            else:
                                self.add_bricks("up", fcount, gap, self.low_wick)
                            self.low_wick = 0
                            self.high_wick = 0
                            gap = d * self.percent / 100
                        else:
                            if d > self.high_wick:
                                self.high_wick = d
                else:
                    if d > self.bricks[-1].close:
                        delta = d - self.bricks[-1].close
                        fcount = math.floor(delta / gap)
                        if fcount != 0:
                            self.add_bricks("up", fcount, gap)
                            gap = d * self.percent / 100
                    if d < self.bricks[-1].close:
                        delta = self.bricks[-1].close - d
                        fcount = math.floor(delta / gap)
                        if fcount != 0:
                            self.add_bricks("down", fcount, gap)
                            gap = d * self.percent / 100

        pbrenko = PBRenko(
            bricks=self.bricks,
            percent=self.percent,
            number_of_leaks=self.number_of_leaks
        )
        return pbrenko


    def add_bricks(self, type, count, brick_size, wick=0):
        if type != self.bricks[-1].type and count > 1:
            self.number_of_leaks = self.number_of_leaks + 1 
        for i in range(count):
            if type == "up":
                if self.bricks[-1].type == "up" or self.bricks[-1].type == "first":
                    if wick == 0:
                        self.bricks.append(Brick(type=type, open=self.bricks[-1].close, close=(self.bricks[-1].close + brick_size), low=self.bricks[-1].close, high=(self.bricks[-1].close + brick_size)))
                    else:
                        if i == 0:
                            self.bricks.append(Brick(type=type, open=self.bricks[-1].close, close=(self.bricks[-1].close + brick_size), low=wick, high=(self.bricks[-1].close + brick_size)))
                        else:
                            self.bricks.append(Brick(type=type, open=self.bricks[-1].close, close=(self.bricks[-1].close + brick_size), low=self.bricks[-1].close, high=(self.bricks[-1].close + brick_size)))
                elif self.bricks[-1].type == "down":
                    if wick == 0:
                        self.bricks.append(Brick(type=type, open=self.bricks[-1].open, close=(self.bricks[-1].open + brick_size), low=self.bricks[-1].open, high=(self.bricks[-1].open + brick_size)))
                    else:
                        if i == 0:
                            self.bricks.append(Brick(type=type, open=self.bricks[-1].open, close=(self.bricks[-1].open + brick_size), low=wick, high=(self.bricks[-1].open + brick_size)))
                        else:
                            self.bricks.append(Brick(type=type, open=self.bricks[-1].open, close=(self.bricks[-1].open + brick_size), low=self.bricks[-1].open, high=(self.bricks[-1].open + brick_size)))
            elif type == "down":
                if self.bricks[-1].type == "up":
                    if wick == 0:
                        self.bricks.append(Brick(type=type, open=self.bricks[-1].open, close=(self.bricks[-1].open - brick_size), high=self.bricks[-1].open, low=(self.bricks[-1].open - brick_size)))
                    else:
                        if i == 0:
                            self.bricks.append(Brick(type=type, open=self.bricks[-1].open, close=(self.bricks[-1].open - brick_size), high=wick, low=(self.bricks[-1].open - brick_size)))
                        else:
                            self.bricks.append(Brick(type=type, open=self.bricks[-1].open, close=(self.bricks[-1].open - brick_size), high=self.bricks[-1].open, low=(self.bricks[-1].open - brick_size)))
                elif self.bricks[-1].type == "down" or self.bricks[-1].type == "first":
                    if wick == 0:
                        self.bricks.append(Brick(type=type, open=self.bricks[-1].close, close=(self.bricks[-1].close - brick_size), high=self.bricks[-1].close, low=(self.bricks[-1].close - brick_size)))
                    else:
                        if i == 0:
                            self.bricks.append(Brick(type=type, open=self.bricks[-1].close, close=(self.bricks[-1].close - brick_size), high=wick, low=(self.bricks[-1].close - brick_size)))
                        else:
                            self.bricks.append(Brick(type=type, open=self.bricks[-1].close, close=(self.bricks[-1].close - brick_size), high=self.bricks[-1].close, low=(self.bricks[-1].close - brick_size)))
