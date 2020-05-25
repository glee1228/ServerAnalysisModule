import os

class FightDetectionModule:
    model = None
    # result = None
    path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.model_name = "FightDetectionModule"
        self.result = []


    def analysis_from_json(self, pe_result,od_result,intermediate_features):
        # pe_result : [frame_num, object_index, x1,y1,conf1,x2,y2,cof2,...,x17,y17,conf17]
        # od_result : [frame_num, object_index, x1,x2,y1,y2,object conf, class conf, class index]
        # intermediate_features : [darknet.conv80.feature,darknet.conv90.feature,conv100.feature]

        # print(pe_result)
        # print(od_result)
        # print(intermediate_features[0].shape,intermediate_features[1].shape,intermediate_features[2].shape)


        return self.result

