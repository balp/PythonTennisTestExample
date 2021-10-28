

class TennisGame:
    #
    # This implemenation is from Emily Bache, with some tweeks and additions by
    # me, see https://github.com/emilybache/Tennis-Refactoring-Kata for original
    # code python/tennis.py (TennisGame3, 68d35aeab8ebc77178d47552ec2a1f9138b8d269)
    #
    # The MIT License (MIT)
    #
    # Copyright (c) 2015 @emilybache
    #
    # Permission is hereby granted, free of charge, to any person obtaining a copy
    # of this software and associated documentation files (the "Software"), to deal
    # in the Software without restriction, including without limitation the rights
    # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    # copies of the Software, and to permit persons to whom the Software is
    # furnished to do so, subject to the following conditions:
    #
    # The above copyright notice and this permission notice shall be included in
    # all copies or substantial portions of the Software.
    #
    # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    # THE SOFTWARE.

    def __init__(self, player1name: str, player2name: str):
        self.p1N = player1name
        self.p2N = player2name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n: str) -> None:
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self) -> str:
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1) else "Win for " + s

