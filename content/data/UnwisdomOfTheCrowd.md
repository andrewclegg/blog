Title: The unwisdom of the crowd: marketing, metrics &amp; machine learning
Date: 2014-06-16
Tags: analytics, data science, product development, marketing
Summary: "Vanity metrics" is a phrase I've heard cropping up a few times recently, in the context of growth engineering, the lean startup movement, and discussions around product lifecycles. In trying to understand what this refers to, I had a small epiphany: people in the digital marketing world are dismissing really important data as "vanity metrics" because they're *only* talking about aggregates. But the same data at the level of *individuals* can make or break a business. If you're trying to grow, you need to understand this.

#### Or, why Google Analytics is not a good analytics tool.

*This is a slightly modified repost of an article I wrote for an internal Pearson blog recently. My colleague [Tendayi](https://twitter.com/tendayiviki) encouraged me to post it here, so it could reach a wider audience.*

"Vanity metrics" is a phrase I've heard cropping up a few times recently, in the context of growth engineering, the lean startup movement, and discussions around product lifecycles. It's hard to find any agreement on what metrics are vanity metrics, but in general it seems to refer to metrics that product owners measure and report in order to boast about growth, but which don't themselves prove anything about value or guide decision-making. Numbers of logins, of resources viewed, of content items downloaded, or of messages sent &mdash; these might be considered vanity metrics, depending on the product. This seemed a bit strange to me, because in my world, all these metrics are extremely valuable.

Suddenly it occurred to me this morning: when product and marketing experts talk about these metrics, they're almost always referring to *aggregates* &mdash; counts or averages across all users, or specific predefined segments. But when data scientists talk about them, we're often talking about *individual users*.

So why would I want to record and measure login counts or download counts for individual users? Or in the education domain, where I work: why count learning resources viewed, time taken on tasks, etc.? Well, all of these things are essential components of a user profile, and without a good user profile, you can't do things like:

* **Predict** which users will suffer poor educational outcomes
    * Contact those with poor predicted outcomes, to offer them more support
* **Recommend** content to users
    * Educational tasks that are likely to improve their assessment scores
    * Purchases they're likely to make
* **Score** users for loyalty
    * Target low-scoring users in order to reduce churn
* **Estimate** the probability of a given user responding to an offer
    * Tailor offers to specific users in order to lift acceptance rate or overall revenue
* **Explain** negative trends in the behaviour of certain users
    * Substandard educational outcomes
    * Failure to renew subscriptions
    * Low click-through rate on recommendations

... and so on.

Some of these examples are specific to our area of business, and I'm sure you have similar domain-specific challenges, but others apply across the commercial web. And all of them need activity data down to the level of individual users. Something that may seem like a "vanity metric" when reported across all users &mdash; number of logins per week, for example &mdash; can be a very important indicator of an *individual* user's engagement, when it's fed into a machine learning model for risk scoring.

At the top of this article I mentioned Google Analytics. I don't want to pick on GA specifically, as this is common across web analytics tools in general, but I sometimes hear product owners saying "we don't need a way to record user activity, we have Google Analytics already." But this misses the point that GA is designed to report aggregates across all your users, or across segments that you've defined in advance. Unless it's changed considerably since I last used it, GA makes it very hard or impossible to report these metrics for individual users, or for *retrospectively-defined* groups of users that are interesting because of some shared (usually negative) behaviour. And it also makes it hard or impossible to connect the activity of individual users with other elements of a user profile, such as demographic information, educational records, purchase history and so on.

So please take the term "vanity metrics" with a pinch of salt. A particular KPI may be worth very little when reported at the level of your entire user base, but it might be the differentiator between a loyal customer or satisfied learner, a borderline case who needs help and support right now, or a lost cause.

