### Poetry
keyring locked error
```python
  InitError

  Failed to create the collection: Prompt dismissed..

  at ~/.local/share/pypoetry/venv/lib/python3.10/site-packages/keyring/backends/SecretService.py:63 in get_preferred_collection
       59│                 collection = secretstorage.Collection(bus, self.preferred_collection)
       60│             else:
       61│                 collection = secretstorage.get_default_collection(bus)
       62│         except exceptions.SecretStorageException as e:
    →  63│             raise InitError("Failed to create the collection: %s." % e)
       64│         if collection.is_locked():
       65│             collection.unlock()
       66│             if collection.is_locked():  # User dismissed the prompt
       67│                 raise KeyringLocked("Failed to unlock the collection!")
```

using this command in terminal
#### export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring

-------------------------------------------------------------------------------------------------