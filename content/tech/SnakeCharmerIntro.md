Title: Snake Charmer: the all-in-one data science toolbox for Python 3
Date: 2014-06-04
Tags: snake charmer, vagrant, salt, virtualbox, virtualization, python
Summary: Wouldn't it be great if you could magic up an IPython Notebook server, complete with SciPy, Pandas, Matplotlib, PyMC, scikit-learn, R and Octave integration, and much much more, just by typing one command? And wouldn't it be even better if you could do that from pretty much any Windows, Mac or Linux machine, and know that you'd get the exact same environment every time? That's Snake Charmer &mdash; a virtual data workbench that's reproducible, portable, shareable and up-to-date.
 
Python's an amazing language, but it's constantly let down by its packaging and distribution infrastructure. Apologies to those people who've worked hard to fix this, but it sucks. I've wasted days in the past getting a particular set of packages to cooperate on a particular machine, only to find that the resulting combination of library files, symlinks, chicken blood and chanting doesn't work on any *other* machines.

The [virtualenv](http://virtualenv.readthedocs.org/en/latest/) tool helps a bit, by letting you have entirely separate Pythons, different versions if necessary, with their own sandboxed libraries and tools. But not all packages behave well in virtualenvs. Some are just sloppily written, but others have very specific dependencies on libraries supplied by your operating system or compiler toolchain, which may be written in C or Fortran or Ancient Enochian, and can't easily be localized to a virtualenv. Some even have specific hardware requirements, or platform-specific behavioural quirks.

This is particularly true in scientific and statistical computing, where some of the most popular Python tools make use of low-level libraries for linear algebra or parallel computing, and others rely on OS-dependent features for image rendering or interprocess communication. And behavioural differences and incompatibilities can be particularly pernicious &mdash; maybe your code will run without any errors, but quietly produce [slightly inaccurate predictions](https://github.com/statsmodels/statsmodels/issues/1690).

#### Meanwhile, in Shoreditch...

Thankfully, there's a solution to many of these problems, if we borrow an idea from our much hipper web developer friends. These days it's quite common to build standardized, pre-packaged virtual machines (VMs) for developers to work in, meaning your code has the same runtime environment as all your teammates' code does, and this closely resembles the servers you will eventually deploy to. By running a little server inside each developer's laptop or desktop, with its own OS and emulated 'hardware', you mask the differences between all those machines and the software installed on them.

Who cares if Alice has Mountain Lion on a MacBook Air, and Bob has Lucid Lynx on a water-cooled tower PC with a Cylon-themed case mod? When they're building code and running tests, they're both using the exact same version of Debian that their server farm uses. So the scope for incompatibilities is hugely reduced. But Alice and Bob still get to use the same text editors, IDEs and other dev tools they rely on &mdash; their VMs augment the capabilities of their original OSes, but don't replace them. This is not really a new idea, but end-user virtualization tools like [Vagrant](http://www.vagrantup.com/) and automation frameworks such as [Salt](http://www.saltstack.com/community/) have made it much easier.

#### The science bit

My goal with [Snake Charmer](https://github.com/andrewclegg/snake-charmer) is to provide the same hassle-free experience to scientists, engineers, statisticians and data miners. Any two VMs built from the same Snake Charmer config should behave exactly the same, even if they're on a completely different hardware or OS platform. And installation needs to be as smooth as possible. When you run Snake Charmer, it does the following, *entirely unsupervised*, through the mechanisms provided by Vagrant and Salt:

- Downloads a VM image for a specific version of Ubuntu

- Boots this up in [VirtualBox](https://www.virtualbox.org/)

- Installs a precise versioned set of Ubuntu packages, including Python 3.4

- Installs an equally exact list of Python packages, patching them where necessary so they play well together

- Starts up an IPython Notebook server on the VM, and gives you its URL

The packages installed include NumPy, SciPy, Pandas, IPython, Matplotlib, Seaborn, scikit-learn, PyMC, statsmodels, PyTables, SymPy, Numexpr, Theano, DEAP, gensim, NLTK, Beautiful Soup, Cython, Numba [and more](https://github.com/andrewclegg/snake-charmer/blob/master/README.md#what-is-included). And it even comes bundled with R and Octave, and connectors to plug these into IPython &mdash; on the slim chance you find something that you really can't do in Python.

Of course, since it's just a standard Ubuntu box running standard Python, you can install whatever other packages you need, from the [Python package index](https://pypi.python.org/pypi), the [Ubuntu repositories](http://packages.ubuntu.com/) or elsewhere. And if there's a package that you need all the time, you can just add it to Snake Charmer's config files so that it gets installed automatically any time you need to build a fresh VM. But that's just the tip of the iceberg. The fact that these are complete virtual machines, not just software packages, brings all kinds of added benefits.

#### Big fish, little fish, virtual box

Here are some of the useful things you can do with VMs, either via Vagrant commands, or through VirtualBox's admin app.

**Disposability.** Normally, you wouldn't store data or code *within* the VM, you would use it to run notebooks and read data files from your physical computer. This means if you mess up your VM somehow, you can just delete it and create a new, identical one. Think of them as disposable commodities that aren't even worth fixing.

**Snapshots and rollbacks.** On the other hand, you might want to make some persistent changes to a VM, like trying out a new package, or a new version of a library. You can take a *snapshot* of a whole VM before making a change or taking an action, and if necessary, undo it by rolling back the whole VM to the snapshot. You could also use this feature to save the state of the VM at intermediate points along an analysis pipeline. It's also a good idea to make a snapshot after you first create a fresh VM, as rolling back is much quicker than installing a new one from scratch.

This process can be managed via a [Vagrant plugin](https://github.com/dergachev/vagrant-vbox-snapshot) or through [VirtualBox itself](http://www.howtogeek.com/150258/how-to-save-time-by-using-snapshots-in-virtualbox/).

**Shareability.** You can bundle up your VM into a [redistributable package](https://docs.vagrantup.com/v2/cli/package.html), including any changes you've made to it, and then send it to your colleagues, or make it available for download. Plus you can include data, notebooks and scripts within the package, meaning your entire workflow can be replicated. I believe this has lots of potential in education and in scientific publishing, beyond the more obvious uses in academic and commercial R&D environments.

**Collaboration.** Using [Vagrant Cloud](https://vagrantcloud.com/), you can easily let remote users [connect to your VMs](http://docs.vagrantup.com/v2/share/index.html) over the internet &mdash; either securely authenticated individuals, or anyone with the URL. This is a natural extension of [IPython's broadcasting features](http://penandpants.com/2013/05/08/broadcasting-ipython-notebooks/), and could be used for collaborative working, running demos, presenting results, or teaching. In general, it won't be affected by firewalls, broadband NAT etc.

**Resource management.** You can put [hard limits](https://github.com/andrewclegg/snake-charmer/blob/master/CUSTOMIZING.md#environment-variables) on the amount of memory, CPU and storage space a VM can consume, so a runaway process can't crash your whole computer. (We've all been there...) And you can [suspend](https://docs.vagrantup.com/v2/cli/suspend.html) a running VM, freeing up all the resources it's using, even if it's in the middle of a long-running task &mdash; then [resume](https://docs.vagrantup.com/v2/cli/resume.html) where you left off later.

**Elasticity.** If your resource limits are too tight, for example there's not enough RAM to build a model in, you can extend them any time. If there's not enough *physical* RAM, CPU or disk space in your computer, you can move the entire VM to a server &mdash; or simply create a new, identical one there. With a bit of extra work you can even host a Snake Charmer VM on cloud services like [Amazon EC2](https://github.com/mitchellh/vagrant-aws) and professional virtualization platforms like [VMWare](http://docs.vagrantup.com/v2/vmware/index.html). And you could even create an [IPython cluster](http://ipython.org/ipython-doc/stable/parallel/parallel_intro.html) of identical VMs for parallel processing.

#### What next?

It's still early days for Snake Charmer, which currently provides one version of Python (3.4) on one version of Ubuntu (12.04), and installs over 25 data science packages. I want to keep adding new packages on a regular basis, and stay reasonably up-to-date with new versions of Python and Ubuntu. I plan to create a Python 2.7 build too. At some point in the future it might be possible for me to host pre-built VM images for download, but that would need a sponsor, as I want to keep it entirely free.

To get started, [clone the git repository](https://github.com/andrewclegg/snake-charmer), and follow the steps in the [README](https://github.com/andrewclegg/snake-charmer/blob/master/README.md). All you really need to do is install VirtualBox and Vagrant, and run one command. Please let me know how you get on, either here or [on Twitter](https://twitter.com/andrew_clegg).

*Note: A previous version of this post talked about 'official releases' but I've since decided not to do numbered releases. The reason being, it gives a false sense of permanence. A third-party package listed in a numbered release can still [disappear from a repo](https://github.com/andrewclegg/snake-charmer/commit/83932610d1f04486351094de2e2ddcc292d64e93) which will break a numbered release. It's probably better just to ensure that master at any point in time is a valid build. Happy to hear any alternative ideas you might have...*

