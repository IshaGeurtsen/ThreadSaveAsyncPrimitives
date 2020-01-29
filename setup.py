import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thread_save_async_primitives-steviestickman",
    version="0.0.2",
    author="steviestickman",
    author_email="139a414@gmail.com",
    description="A collection of thread save async primitives such as Locks for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/steviestickman/ThreadSaveAsyncPrimitives",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
