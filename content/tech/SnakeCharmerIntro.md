Title: Snake Charmer: the all-in-one data science toolbox for Python 3
Date: 2014-06-04
Tags: snake-charmer, vagrant, salt, virtualbox, virtualization
Summary: Python's package management has always been a weakness, but virtualization tools offer a way out. With Snake Charmer you can create a full-stack data science environment with a single command, including most major Python packages for data analysis, statistical modelling, machine learning, mathematical programming and visualization. And what's more, it'll be reproducible, portable, and shareable with your colleagues and peers. Here's how it works.
 
Python's an amazing language, but it's constantly let down by its packaging and distribution infrastructure. Apologies to those people who've worked hard to fix this, but it sucks. I've wasted days in the past getting a particular set of packages to cooperate on a particular machine, only to find that the resulting combination of library files, symlinks, chicken blood and chanting doesn't work on any *other* machines.

The [virtualenv](http://virtualenv.readthedocs.org/en/latest/) tool helps a bit, by letting you have entirely separate Pythons, different versions if necessary, with their own sandboxed libraries and tools. But not all packages behave well in virtualenvs. Some are just sloppily written, but others have very specific dependencies on libraries supplied by your operating system or compiler toolchain, which may be written in C or Fortran or Enochian, and can't easily be localized to a virtualenv. Some even have specific hardware requirements.

This is particularly true in data science, where some Python tools make use of low-level libraries for linear algebra or parallel computing, and others rely on OS-dependent features for image rendering or interprocess communication. And behavioural differences and incompatibilities can be particularly pernicious &mdash; maybe your code will run without any errors, but quietly produce [slightly inaccurate predictions](https://github.com/statsmodels/statsmodels/issues/1690).

#### Meanwhile, in Shoreditch...

Thamkfully, there's a solution to all this, if we borrow an idea from our skinny-trousered web developer friends. These days it's quite common to build standardized, pre-packaged virtual machines (VMs) for developers to work in, meaning you have the same development environment as all your teammates, and it closely resembles the environment found on your servers. By running a little server inside each developer's laptop or desktop, with its own OS and emulated 'hardware', you mask the differences between all those machines and the software installed on them.

Who cares if Alice has Mountain Lion on a MacBook Air, and Bob has Lucid Lynx on a water-cooled tower PC with a Cylon-themed case mod? When they're building the code and running the tests, they're both using the exact same version of Debian that their server cloud uses. So the scope for incompatibilities is hugely reduced. This is not really a new idea, but developer-centric desktop virtualization tools like Vagrant have made it much easier.

#### The science bit

My goal with Snake Charmer is to provide the same hassle-free experience to scientists, engineers, statisticians and analysts. When you run Snake Charmer, it does the following, entirely unsupervised, with a little help from Vagrant and Salt:

- Downloads a VM image for a specific version of Ubuntu

- Boots this up in VirtualBox

- Installs a precise versioned set of Ubuntu packages, including Python 3.4, via Salt

- Installs an equally exact list of Python packages, again via Salt, patching them where necessary so they play well together

- Starts up an IPython Notebook server on the VM, and gives you its URL

The packages installed include NumPy, SciPy, Pandas, IPython, Matplotlib, Seaborn, scikit-learn, PyMC, statsmodels, PyTables, SymPy, Numexpr, Theano, DEAP, gensim, NLTK, Beautiful Soup, Cython, Numba and more. And it even comes bundled with R and Octave, and connectors to plug these into IPython &mdash; on the slim chance you find something that you really can't do in Python.

Of course, since it's just a standard Ubuntu box running standard Python, you can install whatever other packages you need. But that's just the tip of the iceberg. The fact that it's a VM brings all kinds of added benefits.


