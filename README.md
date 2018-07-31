请停止使用该脚本，目前腾讯云已全面支持HAVIP！！！！！！！

产品文档：https://cloud.tencent.com/document/product/215/18025?!preview=true&lang=zh

基本介绍

产品形态如下： 
 - HAVIP是一个内网IP，有子网属性，只能被同一个子网的机器的网卡绑定； 
 - 完全浮动，由后端的机器进行来决定宣告，支持抢占式和非抢占式； 




[在放置之前请先根据文档（ https://www.qcloud.com/community/article/804074 ）将相关公有参数修改为自身真实的参数]

[Before placing, modify the relevant public parameters to their own true parameters according to the document (in addition)]

将所有脚本放在QCloud Python ADK同一目录下

Put all scripts in the same directory as QCloud python ADK

然后运行./check.sh & 即可，一秒一次探测

Then run ./check.sh &,detection per second

run ./check.sh &
