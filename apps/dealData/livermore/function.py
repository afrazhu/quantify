import json
import sys
import os

# common file
sys.path.append("../../../common/")
from Constant import const

class Function(object):

    def getType(self, preValue, lastValue, percent, nowPrice):
        type = ""
        comparePrice = 0
        preType = preValue.get("preType")
        if preType == const.ONE_UP:

            if percent >= const.KEY_MAX:
                type = const.TWO_DOWN

        elif preType == const.TWO_UP:

            if const.TWO_DOWN in lastValue:
                comparePrice = float(lastValue.get(const.TWO_DOWN))

            if percent >= const.KEY_MAX:
                if comparePrice and nowPrice > comparePrice:
                    type = const.THREE_DOWN
                else:
                    type = const.TWO_DOWN
            elif percent <= -const.KEY_MIN:
                type = const.ONE_UP

        elif preType == const.THREE_UP:

            if const.TWO_UP in lastValue:
                comparePrice = float(lastValue.get(const.TWO_UP))
                if comparePrice and nowPrice > comparePrice:
                    type = const.TWO_UP


        elif preType == const.ONE_DOWN:

            if percent <= -const.KEY_MAX:
                type = const.TWO_UP

        elif preType == const.TWO_DOWN:

            if const.TWO_UP in lastValue:
                comparePrice = float(lastValue.get(const.TWO_UP))

            if percent <= -const.KEY_MAX:
                if comparePrice and nowPrice < comparePrice:
                    type = const.THREE_UP
                else:
                    type = const.TWO_UP
            elif percent >= const.KEY_MIN:
                type = const.ONE_DOWN

        elif preType == const.THREE_DOWN:

            if const.TWO_DOWN in lastValue:
                comparePrice = float(lastValue.get(const.TWO_DOWN))
                if comparePrice and nowPrice < comparePrice:
                    type = const.TWO_DOWN

        return type



    def geneNowType(self, preValue, lastValue, nowPrice):
        if not preValue:
            type = const.INIT
        else:
            prePrice = float(preValue.get("prePrice"))
            percent = (nowPrice - prePrice) / prePrice * 100
            percent = round(percent)
            type = self.getType(preValue, lastValue, percent, nowPrice)
        return type

    def getPreValue(self, file):
        checkExists = os.path.exists(file)
        print(checkExists)
        if checkExists:
            with open(file, 'r') as f:
                datas = json.load(f)
                return datas
        else:
            return {}

function = Function()