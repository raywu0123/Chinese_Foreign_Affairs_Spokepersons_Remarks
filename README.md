# Chinese Foreign Affairs Spokeperson's Remarks


## Data
* If you just want the data, it's at `qa.txt`.

### Format
```text
Q:question from a journalist
A:remarks of the spokeperson

Q:question from a journalist
A:remarks of the spokeperson
...
```

### Examples
```text
Q:据报道，美国国会众议院当地时间28日下午审议通过了“2019年西藏政策及支持法案”，中方对此有何评论？ 
A:美国国会众议院通过所谓的“2019年西藏政策及支持法案”，此举严重违反国际法和国际关系基本准则，粗暴干涉中国内政，向“藏独”势力发出严重错误信号。中方对此表示强烈愤慨、坚决反对。 西藏自古以来就是中国领土。西藏事务纯属中国内政，不容任何外部势力干涉。过去60多年来，西藏经济社会文化生态等各领域都取得了历史性发展变化。当前，西藏经济持续健康发展，社会大局和谐稳定，各族人民团结互助，宗教和睦佛事和顺，文化繁荣发展，生态环境良好，人民生活不断改善。西藏各族人民衷心拥护中国政府和西藏自治区政府的各项政策，正在同全国人民一道，为全面建成小康社会而努力奋斗。近年来，国际社会越来越了解西藏的真实情况，也越来越理解支持中国的涉藏政策。 涉藏问题不是民族问题和宗教问题，也不是人权问题，而是涉及中国主权和领土完整的重大原则问题。我们敦促美方客观看待西藏经济社会发展成就，充分认清涉藏问题的高度敏感性，立即纠正错误，停止利用涉藏问题干涉中国内政，多做有利于中美互信与合作的事，而不是相反。

Q:28日，美国总统特朗普公布了“中东和平新计划”政治部分内容，中方对此有何评论？
A:中方注意到了有关报道，正在对有关内容进行研究。中方一贯认为，联合国有关决议和“两国方案”、“土地换和平”原则等国际共识构成了解决巴勒斯坦问题的基础，应当得到遵守。任何有关巴勒斯坦问题的解决方案，应该倾听主要当事方特别是巴勒斯坦方面的看法和主张，应该通过平等对话和谈判达成协议，应该有利于推动巴勒斯坦问题早日实现全面、公正、持久解决。
```

## Crawling the Data Yourself

### Requirements
* python3.6+
* requests
* tqdm
* Beatifulsoup4


### Steps
1. Get all page URLs:
    ```
    python get_page_urls.py <page_url_filename>
    ```
    e.g.
    ```
    python get_page_urls.py urls.txt
    ```
    
    * Note: There are two constants at the head of `get_page_urls.py` that may change through time.

2. Crawling the Corpus:
    ```
    python crawl.py <page_url_filename> <corpus_filename>
    ```
    e.g.
    ```
    python crawl.py urls.txt qa.txt
    ```