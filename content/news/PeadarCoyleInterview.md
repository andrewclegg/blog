Title: Interview with a Data Scientist
Date: 2015-06-06
Tags: interviews, data science
Summary: An interview I did for data scientist and blogger Peadar Coyle.

*I was recently interviewed by Peadar Coyle for his data science blog, [Models are Illuminating and Wrong](https://peadarcoyle.wordpress.com/), as the latest in a series of features on people in the field. It's archived here for posterity, but I would recommend taking a look at the [whole collection](https://peadarcoyle.wordpress.com/2015/05/14/interviews-with-data-scientists-the-collection/).*

**1. What project have you worked on do you wish you could go back to, and do better?**

The one that most springs to mind was an analytics and visualization platform called Palomino that my team at Pearson built: a custom JS/HTML5 app on top of Elasticsearch, Hadoop and HBase, plus a bunch of other pipeline components, some open source and some in-house. It kind of worked, and we learnt a lot, but it was buggy, flaky at the scale we tried to push it to, and reliant on constant supervision. And it's no longer in use, mostly for those reasons.

It was pretty ambitious to begin with, but I got dazzled by shiny new toys and the lure of realtime intelligence, and brought in too many new bits of tech that there was no organisational support for. We discovered that distributed data stores and message queues are *never* as robust as they claim (c.f. [Jepsen](https://aphyr.com/tags/jepsen)); that most people don't really need realtime interactive analytics; and that supporting complex clustered applications (even internal ones) is really hard, especially in an organisation that doesn't really have a devops culture.

These days, I'd try very hard to find a solution using existing tools -- [Kibana](https://www.elastic.co/products/kibana) for example looks much more mature and powerful than it did when we started out, and has a whole community and coherent ecosystem around it. And I'd definitely shoot for a much simpler architecture with fewer moving parts and unfamiliar components. Dan McKinley's article [Choose Boring Technology](http://mcfunley.com/choose-boring-technology) is very relevant here.

**2. What advice do you have to younger analytics professionals and in particular PhD students in the Sciences?**

I was asked this the other day by a recent PhD grad who was interested in a data science career, so I'll pass on what I told him.

I think there are broadly three kinds of work that take place under the general heading of "data scientist", although, there are also plenty of exceptions to this.

The first is about turning data into business insight, via statistical modelling, forecasting, predictive analytics, customer segmentation and clustering, survival analysis, churn prediction, visualization, online experiment design, and selection or design of meaningful metrics and KPIs.

The second is about developing data-driven products and features for the web, e.g. recommendation engines, trend detectors, anomaly detectors, search and ranking engines, ad placement algorithms, spam and abuse classifiers, content fingerprinting and similarity scoring, etc.

The third is really a more modern take on what used to be called operational research, i.e. optimizing business processes algorithmically to reduce time or cost, or increase coverage or reported satisfaction.

In many companies these will be separate roles, and not all companies do all three. But you'll also see roles that involve two or occasionally all three of these, in varying proportions. I guess a good start is to think about which appeals to you the most, and that will help guide you.

Don't get confused by the nomenclature: "data scientist" could mean any of those things, or something else entirely that's been rebranded to look cool. And you could be doing any of those things and not be called a data scientist. Read the job specs closely and ask lots of questions.

**3. What do you wish you knew earlier about being a data scientist?**

Well, I wish I'd taken double maths for A level, all those years ago! As it was, I took the single option, and chose the mechanics module over statistics, something that held me back ever since despite various post-graduate courses. There are certain things that are just harder to crowbar into an adult brain, if you don't internalize the concepts early enough. I think languages and music are in that category too.

(For our global readers: A-levels are the qualifications from the last two years of high school. You usually do three or four subjects, or at least you did in my day. You could do standard maths with mechanics or stats, or standard + further with both, which counted as two qualifications.)

I had a similar experience with biology -- I dropped it when I was 16 but ended up working in bioinformatics for several years. Statistics and biology are both subjects that are much more interesting than school makes them seem, and I wish I'd known that at the time.

**4. How do you respond when you hear the phrase 'big data'?**

Well, I used to react with anger and contempt, and have given some [pretty opinionated talks](https://drive.google.com/file/d/0B1HztRme3ZjZZjA1WHFJY25lQnM/view) on that subject before. It's one of those things you can't get away from in the enterprise IT world, but ironically, since I joined Etsy I've been numbed to the phrase by over-exposure... Just because the Github repo for our Scalding and Cascading code is called "BigData".

It's a marketing term with very little information content -- rather like "cloud". But unlike "cloud" I actually think it's actively misleading -- it focuses attention on the size aspect, when most organisations have interesting and potentially valuable datasets that can fit on a laptop, or at least a medium-sized server. For that matter, a server with a *terabyte* of RAM isn't much over $20K these days. "Big data" makes IT departments go all weak-kneed with delight or terror at the prospect of getting a Hadoop (or Spark) cluster, even though that's often not the right fit at all.

And as a noun phrase, it sucks, as it really doesn't refer to anything. You can't say "we solved this problem with big data" as big data isn't really a thing with any consistent definition.

**5. What is the most exciting thing about your field?**

That's an interesting one. Deep learning is huge right now, but part of me still suspects it's a passing fad, partly because I'm old enough to remember when plain-old neural networks were at the same stage of the hype cycle. Then they fell by the wayside for years. That said, the concrete improvements shown by convolutional nets on image recognition tasks are pretty impressive.

Time will tell whether that feat can be replicated in other domains. Recent work on [recurrent nets for modelling sequences](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) (text, music, etc.) is interesting, and there's been some fascinating work from Google (and their acquihires DeepMind) on learning to [play video games](http://arxiv.org/abs/1312.5602) or [parse and execute code](http://arxiv.org/abs/1410.4615). These last two examples both combine deep learning with non-standard training methods (reinforcement learning and curriculum learning respectively), and my money's on this being the direction that will really shake things up. But I'm a layman as far as this stuff goes.

One problem with neural architectures is that they're often black boxes, or at least pretty dark grey -- hard to interpret or gain much insight from. There are still a lot of huge domains where this is a hard sell, education and healthcare being good examples. Maybe someone will invent a learning method with the transparency of decision trees but the power of deep nets, and win over those people in jobs where "just trust the machine" doesn't work.

**6. How do you go about framing a data problem - in particular, how do you avoid spending too long, how do you manage expectations etc. How do you know what is good enough?**

It took me a long time to realise this, but short release cycles with small iterative improvements are the way to go. *Any* result that shows an improvement over your current baseline is a result -- so even if you think there are much bigger wins to be had, get it into production, and test it on real data, while you work on its replacement. (Or if you're in academia, get a quick workshop paper out while you work on its replacement!)

This is also a great way to avoid overfitting, especially if you are in industry, or a service-driven academic field like bioinformatics. Instead of constantly bashing away at the error rate on a well-worn standard test set, get some new data from actual users (or cultures or sensors or whatever) and see if your model holds up in real life. And make sure you're optimizing for the right thing -- i.e. that your evaluation metrics really reflect the true cost of a misprediction.

I worked in natural language processing for quite a while, and I'm sure that field was held back for a while by collective, cultural overfitting to the same-old datasets, like Penn Treebank section 23. There's an [old John Langford article](http://hunch.net/?p=22) about this and other non-obvious ways to overfit, which is always worth a re-read.

*[Original version at Peadar's blog](https://peadarcoyle.wordpress.com/2015/06/06/interview-with-a-data-scientist-andrew-clegg/)*




