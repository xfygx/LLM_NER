# LLM_NER

先生成一堆句子
把句子中的固定密码换成 top 100。这里文件是 TXT。

使用网上的开源工具（在线）加载 TXT， 一个个标注。然后生成出 json 
json 的格式不匹配 spacy, 用 convert2.py 变换成新的 JSON。

这个生成的 JSON，可以使用 vv.py 从一个空的 BERT 模型开始训练，得到一个可用的结果。

下面基于XXX训练一个 transformer 模型
从官网的 https://spacy.io/usage/training#basics 生成一个 base_config.cfg，下载下来。
把 train.spacy 和 dev.spacy 还有 output 目录准备好
使用 convert2bin.py ，把上面的 JSON 生成为 二进制格式。 因为 spacy 3.0 使用新的 二进制格式。
把二进制数据放到 train.spacy 目录中，数据文件的扩展名是 .spcay ，训练程序会自动找这个扩展名的文件

执行 python -m spacy init fill-config base_config.cfg config.cfg 生成 config.cfg 。

执行 python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy --gpu-id 0 开始训练

训练好后，使用 custom_model.py 来使用训练出来的自定义的模型。

开源标注工具repo ：https://github.com/ManivannanMurugavel/spacy-ner-annotator

spacy 数据格式：https://spacy.io/api/data-formats#json-input

在线开源标注工具: https://manivannanmurugavel.github.io/annotating-tool/spacy-ner-annotator/

NER
https://zhuanlan.zhihu.com/p/43061858
https://tech.meituan.com/2020/07/23/ner-in-meituan-nlp.html

如何用GPT大模型解决NER任务？
http://blog.itpub.net/70027828/viewspace-2956678/
