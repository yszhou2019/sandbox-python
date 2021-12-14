用于 default集群 和async集群的final_info_list的统计
1 首先解析文件，解析出来 stamp -> info_list
2 解析的过程中 对时间进行过滤，过滤掉指定时间之前的数据
3 进行匹配
3.1 统计stamp的匹配程度 -> 没有找到stamp的情况存入到 miss_stamp.txt 中(由于在之前会有提前返回，也就是stamp匹配程度不会到达100%，而且会有较大差距)
3.2 对于找到stamp的情况，比对stamp对应的info_list的匹配程度-> 完全一致的占比，不一致的占比，不一致的单独写出来 写入到 miss_match.txt