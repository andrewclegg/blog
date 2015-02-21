Title: Kale: timeseries data mining at Etsy
Date: 2015-02-21
Tags: kale, monitoring, alerting, metrics, anomaly detection, devops, talks
Summary: Etsy loves metrics. Everything that happens in our data centres gets recorded, graphed and stored. But with over a million metrics flowing in constantly, it’s hard for any team to keep on top of all that information. Graphing and alerting don't scale well, so we've started the Kale project, to help make sense of all those time series.
 
*I'm very pleased to announce that my talk proposal on [Kale](https://codeascraft.com/2013/06/11/introducing-kale/) v2 has been accepted by both [Monitorama 2015](http://monitorama.com/index.html) and [Berlin Buzzwords 2015](http://berlinbuzzwords.de/). Here's the abstract.*

#### Signatures, patterns and trends: Timeseries data mining at Etsy

Etsy loves metrics. Everything that happens in our data centres gets recorded, graphed and stored. But with over a million metrics flowing in constantly, it’s hard for any team to keep on top of all that information. Graphing everything doesn’t scale, and traditional alerting methods based on thresholds become very prone to false positives.

That’s why we started Kale, an open-source software suite for pattern mining and anomaly detection in operational data streams. These are big topics with decades of research, but many of the methods in the literature are ineffective on terabytes of noisy data with unusual statistical characteristics, and techniques that require extensive manual analysis are unsuitable when your ops teams have service levels to maintain.

In this talk I’ll briefly cover the main challenges that traditional statistical methods face in this environment, and introduce some pragmatic alternatives that scale well and are easy to implement (and automate) on Elasticsearch and similar platforms. I’ll talk about the stumbling blocks we encountered with the first release of Kale, and the resulting architectural changes coming in version 2.0. And I’ll go into a little technical detail on the fingerprinting algorithms we use for fast approximate querying of metrics and their associated statistical metadata. These techniques have applications in clustering, outlier detection, similarity search and supervised learning, and they are not limited to the data centre but can be applied to any high-volume timeseries data.

*If you can't make it to either of these, videos will hopefully be available online soon afterwards.*

