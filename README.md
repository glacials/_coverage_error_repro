This repository reproduces a bug with an interaction between these three libraries:

- Coverage.py with `dynamic_context = test_function` ("who tests what") set
- pytest with a hook that calls a function that begins with the string "test"
- All obfuscated with pyarmor

Run this script to reproduce the issue:
```sh
./run.sh
```
You should see some error output like:
```
================================================================================================================================================================================================================================================= test session starts =================================================================================================================================================================================================================================================
platform linux -- Python 3.9.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /home/glacials/yourbase/_break_coverage
plugins: mock-3.6.1, cov-2.12.1
collected 1 item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/_pytest/main.py", line 269, in wrap_session
INTERNALERROR>     session.exitstatus = doit(config, session) or 0
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/_pytest/main.py", line 322, in _main
INTERNALERROR>     config.hook.pytest_collection(session=session)
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/hooks.py", line 286, in __call__
INTERNALERROR>     return self._hookexec(self, self.get_hookimpls(), kwargs)
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/manager.py", line 93, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook, methods, kwargs)
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/manager.py", line 84, in <lambda>
INTERNALERROR>     self._inner_hookexec = lambda hook, methods, kwargs: hook.multicall(
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/callers.py", line 208, in _multicall
INTERNALERROR>     return outcome.get_result()
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/callers.py", line 80, in get_result
INTERNALERROR>     raise ex[1].with_traceback(ex[2])
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/callers.py", line 187, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/_pytest/main.py", line 333, in pytest_collection
INTERNALERROR>     session.perform_collect()
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/_pytest/main.py", line 637, in perform_collect
INTERNALERROR>     hook.pytest_collection_modifyitems(
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/hooks.py", line 286, in __call__
INTERNALERROR>     return self._hookexec(self, self.get_hookimpls(), kwargs)
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/manager.py", line 93, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook, methods, kwargs)
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/manager.py", line 84, in <lambda>
INTERNALERROR>     self._inner_hookexec = lambda hook, methods, kwargs: hook.multicall(
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/callers.py", line 208, in _multicall
INTERNALERROR>     return outcome.get_result()
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/callers.py", line 80, in get_result
INTERNALERROR>     raise ex[1].with_traceback(ex[2])
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/pluggy/callers.py", line 187, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>   File "/home/glacials/yourbase/_break_coverage/conftest.py", line 5, in pytest_collection_modifyitems
INTERNALERROR>     w.testify()
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/coverage/context.py", line 41, in should_start_context_test_function
INTERNALERROR>     return qualname_from_frame(frame)
INTERNALERROR>   File "/home/glacials/.pyenv/versions/3.9.6/lib/python3.9/site-packages/coverage/context.py", line 51, in qualname_from_frame
INTERNALERROR>     self = frame.f_locals["self"]
INTERNALERROR> KeyError: 'self'
```