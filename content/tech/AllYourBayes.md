Title: All your Bayes are belong to us! PyMC, PyStan and emcee in Snake Charmer
Date: 2014-06-04
Tags: snake charmer, bayes, bayesian, python, statistics, machine learning 
Summary: PyMC is the most widely-used Python package for Bayesian modelling, learning and inference. But there are loads of other tools out there that may be better fitted to your particular task. I've added two of them to Snake Charmer so you can try them for yourself.


[PyMC](https://github.com/pymc-devs/pymc) is the most widely-used Python package for Bayesian modelling, learning and inference, but it isn't the only choice, by far. [Jake Vanderplas](https://twitter.com/jakevdp) recently posted a pretty detailed comparison of PyMC, [PyStan](http://mc-stan.org/) and [emcee](http://dan.iel.fm/emcee/current/) on [his blog](http://jakevdp.github.io/blog/2014/06/14/frequentism-and-bayesianism-4-bayesian-in-python/), and even if you're not an expert in Bayesian methods (I'm certainly not) I'd recommend you give it a read. It walks you through the same task in all three packages in order to get a feel for how they work, which is a great way to do it.

As well as functionality, speed and accuracy, Jake also covered installation, and mentioned that PyStan can be painful to install, especially if you don't already have a full C/C++ toolset. While many Linux users do, these days a lot of Mac users don't, and I'd hazard a guess that *most* Windows users don't, even if they program in other languages frequently. Many Python packages need to compile native code during installation, but some of them get round this by offering binaries for various platforms -- although this often not a foolproof solution either. But PyStan also uses the compiler at *runtime*, in the process of translating its own model definition language into machine code, so I guess there's no easy way for them to build a one-click installer.

This is exactly the kind of reason why I started [Snake Charmer](https://github.com/andrewclegg/snake-charmer) in the first place. Installing it and getting the tests passing on Snake Charmer's Ubuntu VM was -- well not entirely trivial, but an hour or two at the very most. And once it works for me, it works for everyone. You'll now get PyStan and the slightly less fiddly emcee as standard with every Snake Charmer VM -- so, err, forget your unpleasant prior experiences and raise your expectations. (Sorry...)

I think this makes Snake Charmer the first Python distribution to include all three of these tools.

One last note: if you try to reproduce Jake's tutorial in Snake Charmer, you may notice some differences. He uses PyMC 2 but Snake Charmer's on a pre-release of version 3 already. (Given limited time to work on this, I'd rather stay ahead of the game...) However, here's a [note from Thomas Wiecki](http://jakevdp.github.io/blog/2014/06/14/frequentism-and-bayesianism-4-bayesian-in-python/#comment-1436231209) showing the equivalent steps in PyMC 3.

