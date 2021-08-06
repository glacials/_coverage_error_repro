This repository reproduces a bug with an interaction between Coverage.py and some types of frames, which I've specifically seen come out of pyarmor. See https://github.com/nedbat/coveragepy/pull/1210

Run this script to reproduce the issue:
```sh
./run.sh
```
You should see some error output like:
```
...
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/coverage/context.py", line 41, in should_start_context_test_function
INTERNALERROR>     return qualname_from_frame(frame)
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/coverage/context.py", line 51, in qualname_from_frame
INTERNALERROR>     self = frame.f_locals["self"]
INTERNALERROR> KeyError: 'self'
```