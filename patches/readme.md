# README

These are all the patch files that I made for OP-TEE with a little description
of what they do and how they work.

## First what are patch-files?

Patch files are generated from a git diff with the following command:

```bash
git diff > patch.patch
```

This is another option which can be used with `git am`:

```bash
git format-patch {{origin}}
```

This patch can the be reapplied with the command:

```bash
git apply /path/to/patch.patch
```

If you used `git format-patch`:

```bash
git am /path/to/patch.patch
```

This creates a new commit which can be signed off, `git apply` on the other hand does not create a new commit.

Patch files where chosen to substitute a full fork of the project and provide an easy fix to the _"unknown zero HUK problem"_.
For the patches `git diff` and `git apply` where used.

## Index of all the patch files

There are several patches in this directory those are listed here with a little description:

1. `keylogger.patch` -- logs keys to the secure world console using the `trace.h` library
2. `stats.patch` -- single patch file for backup purposes for the stats application misses the
   header file stuff (can be ignored)
3. `xtest_stats.patch` -- this file should be applied to the `optee_test` project and patches the
   command line part of the `xtest` application to test for zero HUK
4. `zero-huk.patch` -- this part should be applied to the `optee_os` project and patches the PTA
   `stats.c` and the header file to include the new command `pta_stats.h`. **This only tests for
   zero huk and could be non compatible with the command line application patch**
5. `zero_huk_default_chip.patch` patches the `optee_os` project to detect zero huk and default chip
   id or one of them.

The patches that where applied for the Studienarbeit are 3 `xtest_stats.patch` and 5
`zero_huk_default_chip.patch`. Apply those...
Full paths for the files can be read out of the patch file.
