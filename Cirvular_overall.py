
loading = 0     # 装货指令
unloading = 0   #  卸货指令
backing = 0  # 返回指令

loading_flag = 0 # 到达装货区
unloading_flag = 0
starting_flag = 0

stop_line_flag = 0
traffic_finish_flag = 0
s_start_flag = 0
s_finish_flag = 0

while 1:
    flag = 1
    loading = int(input("loading:"))
    while flag:
        if loading == 1:     # 是否接收到前往装货区指令（loading）
            print('car state: go to Loading area')  # 前往装货区
            loading_flag = int(input('read loading_flag:'))
            while flag:
                if loading_flag == 1: #  是否到达装获区
                    print('car state: arrive at Loading area')  # 到达装获区
                    unloading = int(input('read unloading:'))
                    while flag:
                        if unloading == 1:  # 是否收到卸货指令
                            print('car state: go to stop line')  # 前往停止线
                            stop_line_flag = int(input('read stop_line_flag:'))
                            while flag:
                                if stop_line_flag == 1:              # 是否到达停止线
                                    print('car state: arrive at stop line')  # 到达停止线
                                    print('car state: traffic module')   # 交通灯模块
                                    traffic_finish_flag = int(input('read traffic_finish_flag:'))
                                    while flag:
                                        if traffic_finish_flag == 1:  # 是否完成交通灯
                                            print('car state: go to unloading area')  # 前往卸货区
                                            unloading_flag = int(input('read unloading_flag:'))
                                            while flag:
                                                if unloading_flag == 1:  # 是否到达卸货区
                                                    print('car state: arrive at unloading area')  # 到达卸货区
                                                    backing = int(input("backing:"))
                                                    while flag:
                                                        if backing == 1:
                                                            print('car state: go to s start point')  # 到达卸货区
                                                            s_start_flag = int(input("s_start_flag:"))
                                                            while flag:
                                                                if s_start_flag == 1:
                                                                    print('car state: s road module ')  # s路模块
                                                                    s_finish_flag = int(input("s_finish_flag:"))
                                                                    while flag:
                                                                        if s_finish_flag == 1:
                                                                            print('car state: go to start area')  # 前往开始位置
                                                                            starting_flag = int(input("starting_flag:"))
                                                                            while flag:
                                                                                if starting_flag == 1:
                                                                                    print('car state: arrive at start area')   # 到达开始位置
                                                                                    print('car state: ready')
                                                                                    flag = 0
                                                                                else:
                                                                                    starting_flag = int(input("starting_flag:"))
                                                                                    print('car state: go to start area')  #  前往开始位置
                                                                        else:
                                                                            print('car state:s road module')  # 前往开始位置
                                                                            s_finish_flag = int(input("s_finish_flag:"))
                                                                else:
                                                                    print('car state: go to s start point')  # 到达卸货区
                                                                    s_start_flag = int(input("s_start_flag:"))
                                                        else:
                                                            print('car state: arrive at unloading area')  # 到达卸货区
                                                            backing = int(input("backing:"))
                                                else:
                                                    print('car state: go to unloading area')  # 前往卸货区
                                                    unloading_flag = int(input('read unloading_flag:'))
                                        else:
                                            print('car state: traffic module')
                                            traffic_finish_flag = int(input('read traffic_finish_flag:'))

                                else:
                                    print('car state: go to stop line')
                                    stop_line_flag = int(input('read stop_line_flag:'))
                        else:
                            print('car state: arrive at Loading area')  # 停留装货区
                            unloading = int(input('read unloading:'))

                else:
                    print('car state: go to Loading area')
                    loading_flag = int(input('read loading_flag:'))
        else:
            print('car state: ready')
            loading = int(input("loading:"))


