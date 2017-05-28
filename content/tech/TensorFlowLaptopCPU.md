Title: Optimizing TensorFlow for your laptop's CPU
Date: 2017-05-28
Tags: tensorflow, machine learning, deep learning, osx, macos, mac
Summary: If you don't have access to a server with a cutting-edge GPU, it's worth building TensorFlow from scratch on your laptop or desktop Mac, to squeeze more performance out of it.

I've recently been teaching myself [TensorFlow](https://www.tensorflow.org), and haven't spent the time and money to set up a cloud server (or physical machine!) with a GPU. I was originally running it from a pre-built Docker image, inside a Jupyter notebook, and saw a bunch of warnings like this in the console output:

    W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE3 instructions, but these are available on your machine and could speed up CPU computations.
    W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
    W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
    W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
    W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
    W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.

The pre-built versions available through Docker, pip etc. tend to go for wide compatibility, which means disabling a bunch of optional speedups that aren't supported on all hardware. Thankfully, it turns out not to be too hard to build it from scratch yourself, which lets you switch all this good stuff on, and makes the process of experimentation and learning a bit less tedious.

This could also be useful if you're training a model that's just too damn big to fit on GPU hardware that you can actually afford, or if you want to train on GPUs but squeeze extra performance out of cheap CPU-based inference servers at query time.

Here's a walkthrough of how I did it, on a 2016 Macbook Pro running Sierra (10.12.5). I expect the steps for Windows and Linux are similar. There are quite a few prerequisites, but it's fairly likely you have some of these already.

### Xcode

First off you'll need Xcode if you don't already have it, you can get this from the App Store.

### Python

TensorFlow works with various different versions of Python, I believe, but I was using the [Anaconda distribution](https://www.continuum.io/downloads) of Python 2.7.

### Homebrew

You'll need this if you don't have it already, in order to install Bazel (see below). Download it from [here](https://brew.sh).

### Java

Bazel also requires JDK8 which you can get from [Oracle](http://www.oracle.com/technetwork/java/javase/downloads/index.html). I used 1.8.0_131 which was the latest at time of writing, but I don't think it matters too much.

### Bazel

[Bazel](https://bazel.build) is Google's build tool which is used to compile and package TF. Once Homebrew and Java are installed -- you may want to log out and log back in again to make sure environment variables etc. are set up right -- you can install Bazel by typing:

    brew install bazel

### TensorFlow

Finally we can actually install TensorFlow itself.

I created a Conda environment to work in, first:

    conda create -n tensorflow
    source activate tensorflow

Although I think this is a bit moot, as the pip install step (see below) seems to install it into your Conda site-packages and make it available in all environments automatically.

Then checkout TensorFlow from [GitHub](https://github.com/tensorflow/tensorflow) and cd into your local copy, and

    ./configure

to configure the build. You can switch on various optional features here, it's probably fine to leave everything as defaults though. The actual options we're interested in aren't controlled here, but via command line params when you actually build it.

That's done by typing the following:

    bazel build -c opt --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-msse4.2 -k //tensorflow/tools/pip_package:build_pip_package

This will compile TF itself, and also output a script to generate a Python package. Be warned, this will take a while! Well over an hour, probably more like two. I didn't time it exactly.

On some platforms you need to add `--copt=-mfpmath=both` to the set of flags above, but recent versions of clang provided with macOS don't need this, and will barf if you do.

Once it's finished, you need to bundle it into a pip wheel -- a binary distribution with a Python wrapper:

    bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg

Then you can install this into your Conda environment. First, double-check your paths are set up right by typing `which pip` -- it should be pointing to a version of pip in your anaconda install directory. Then type:

    pip install /tmp/tensorflow_pkg/tensorflow-<blah>.whl

where <blah> is some long version string. Just tab-complete it -- this should be the only .whl file in that directory anyway.

Now we can test it works! But before that, and **this is important**, cd out of the tensorflow directory to somewhere completely different, e.g. your home directory. If you don't do this, when you try to import the package, Python will try to import it from the local directory and not the installed library, and fail with a cryptic error. This confused me the first time.

Anyway, to test it's installed OK, run python or ipython, and:

    import tensorflow as tf
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello))

If this prints a message with no errors, you're good to go.

And we're done! I didn't do any specific speed comparisons but training and evaluating toy models was noticeably faster with the custom build than it had been before. Of course, some of this may be down to the Docker virtualization overhead, not just the CPU flags, but a win's a win -- and you save a load of memory by not using Docker too.


