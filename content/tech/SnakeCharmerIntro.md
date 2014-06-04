Title: Snake Charmer: the all-in-one data science toolbox for Python 3
Date: 2014-06-04
Tags: snake-charmer, vagrant, salt, virtualbox, virtualization
Summary: Wouldn't it be great if you could magic up an IPython Notebook server, complete with SciPy, Pandas, Matplotlib, PyMC, scikit-learn, R and Octave integration, and much much more, just by typing one command? And wouldn't it be even better if you could do that from pretty much any Windows, Mac or Linux machine, and know that you'd get the exact same environment every time? That's Snake Charmer &mdash; a virtual data workbench that's reproducible, portable, shareable and up-to-date.
 
Python's an amazing language, but it's constantly let down by its packaging and distribution infrastructure. Apologies to those people who've worked hard to fix this, but it sucks. I've wasted days in the past getting a particular set of packages to cooperate on a particular machine, only to find that the resulting combination of library files, symlinks, chicken blood and chanting doesn't work on any *other* machines.

The [virtualenv](http://virtualenv.readthedocs.org/en/latest/) tool helps a bit, by letting you have entirely separate Pythons, different versions if necessary, with their own sandboxed libraries and tools. But not all packages behave well in virtualenvs. Some are just sloppily written, but others have very specific dependencies on libraries supplied by your operating system or compiler toolchain, which may be written in C or Fortran or Ancient Enochian, and can't easily be localized to a virtualenv. Some even have specific hardware requirements.

This is particularly true in data science, where some Python tools make use of low-level libraries for linear algebra or parallel computing, and others rely on OS-dependent features for image rendering or interprocess communication. And behavioural differences and incompatibilities can be particularly pernicious &mdash; maybe your code will run without any errors, but quietly produce [slightly inaccurate predictions](https://github.com/statsmodels/statsmodels/issues/1690).

#### Meanwhile, in Shoreditch...

Thamkfully, there's a solution to all this, if we borrow an idea from our much hipper web developer friends. These days it's quite common to build standardized, pre-packaged virtual machines (VMs) for developers to work in, meaning your code has the same runtime environment as all your teammates' code does, and this closely resembles the servers you will eventually deploy to. By running a little server inside each developer's laptop or desktop, with its own OS and emulated 'hardware', you mask the differences between all those machines and the software installed on them.

Who cares if Alice has Mountain Lion on a MacBook Air, and Bob has Lucid Lynx on a water-cooled tower PC with a Cylon-themed case mod? When they're building code and running tests, they're both using the exact same version of Debian that their server farm uses. So the scope for incompatibilities is hugely reduced. But Alice and Bob still get to use the same text editors, IDEs and other dev tools they rely on &mdash; their VMs augment the capabilities of their original OSes, but don't replace them. This is not really a new idea, but end-user virtualization tools like [Vagrant](http://www.vagrantup.com/) and automation frameworks such as [Salt](http://www.saltstack.com/community/) have made it much easier.

#### The science bit

My goal with Snake Charmer is to provide the same hassle-free experience to scientists, engineers, statisticians and data miners. When you run Snake Charmer, it does the following, entirely unsupervised, through the mechanisms provided by Vagrant and Salt:

- Downloads a VM image for a specific version of Ubuntu

- Boots this up in [VirtualBox](https://www.virtualbox.org/)

- Installs a precise versioned set of Ubuntu packages, including Python 3.4

- Installs an equally exact list of Python packages, patching them where necessary so they play well together

- Starts up an IPython Notebook server on the VM, and gives you its URL

The packages installed include NumPy, SciPy, Pandas, IPython, Matplotlib, Seaborn, scikit-learn, PyMC, statsmodels, PyTables, SymPy, Numexpr, Theano, DEAP, gensim, NLTK, Beautiful Soup, Cython, Numba [and more](https://github.com/andrewclegg/snake-charmer/blob/master/README.md#what-is-included). And it even comes bundled with R and Octave, and connectors to plug these into IPython &mdash; on the slim chance you find something that you really can't do in Python.

Of course, since it's just a standard Ubuntu box running standard Python, you can install whatever other packages you need, from the [Python package index](https://pypi.python.org/pypi), the [Ubuntu repositories](http://packages.ubuntu.com/) or elsewhere. And if there's a package that you need all the time, you can just add it to Snake Charmer's config files so that it gets installed automatically any time you need to build a fresh VM. But that's just the tip of the iceberg. The fact that these are complete virtual machines, not just software packages, brings all kinds of added benefits.

#### Big fish, little fish, virtual box

Here are some of the reasons VMs are cool.

**Reproducibility.** Any two VMs built from the same Snake Charmer config will behave exactly the same, even if they're on a completely different hardware or OS platform.

**Shareability.** You can bundle up your VM into a redistributable package, including any changes you've made to it, which you can then send to your colleagues or make available for download. Plus you can include data and notebooks or scripts within the package, creating a complete snapshot of your analysis pipeline at a distinct point in time.

**Collaboration.** TODO Vagrant Cloud

**Robustness.** TODO disposability, rollbacks

**Resource management.** You can put hard limits on the amount of memory, CPU and storage space a VM can consume, so a runaway process can't crash your whole computer. (We've all been there...) And you can suspend a running VM, freeing up all the resources it's using, even if it's in the middle of a long-running task &mdash; then resume where you left off later.

**Elasticity.** If your resource limits are too tight, for example there's not enough RAM to build a model in, you can extend them any time. If there's not enough *physical* RAM, CPU or disk space in your computer, you can move the entire VM to a server &mdash; or simply create a new, identical one there. With a bit of extra work you can even host a Snake Charmer VM on cloud services like Amazon EC2.


