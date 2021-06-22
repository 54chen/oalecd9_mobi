# oalecd9_mobi

通过网上流行的《牛津高阶英汉双解词典第9版》的mdx文件，转到mobi版本，给kindle使用。

先要转成appleDict的版本，再利用他的xml转成mobi的版本。直接用pyglossory转mobi的话，基本上没法用。

先运行： 

pyglossary --write-format=AppleDict "~/Downloads/dict/xxx.mdx" xxxx_Dictionary

里面会有一个xml是全部的词典内容。复制出来备用。相关细节请参考 http://blog.54chen.com/post/mac-add-dictionary/

然后运行这里的transfer.py生成100个词一个小文件到xhtml文件夹里。

再用amazon的kindlegen来产生最终的 oalecd9.mobi。 复制到kindle启用词典即可。

kindlegen oalecd.opf


1.xml有点大，传不上来，需要的email我 czhttp@gmail.com

screenshot
----------

![Screenshot](https://github.com/54chen/oalecd9_mobi/blob/main/1.jpg)

![Screenshot](https://github.com/54chen/oalecd9_mobi/blob/main/2.jpg)

