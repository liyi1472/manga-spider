# 图片爬虫

[**漫画堆**](https://manhua.fzdm.com) 爬虫。

经验：通过 JavaScript 加载的资源不一定需要使用 Splash，关键信息可能就藏在页面的 JavaScript 代码之中。

正则：`.*` 是贪婪模式，`.*?` 就是非贪婪模式了。