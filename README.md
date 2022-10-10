Dstny's matrix.org synapse server
=================================

This is essentially a fork of the matrix.org synapse server github repo. The goal is that we can keep tracking upstream, while still being able to apply patches to the synapse server.

Development workflow
--------------------

Patches to the upstream synapse server are applied with quilt. The patches are stored in the `patches` subdirectory.

If you need to make any changes to synapse for whatever reason, first apply all the patches:
```
quilt push -a
```

Then, start a new patch:
```
quilt new <patch_name>
```

Then, before editing any files, specify which files need to be added to the patch:
```
quilt add <file_x> <file_y>
```

Now edit the files, and then refresh the patch:
```
quilt refresh
```

You can also edit and add to the patch directly:
```
quilt edit <file_x>
```

To remove all patches from the source tree:
```
quilt pop -a
```

Now add the patches to the git stage and commit them as usual

Pulling from upstream
---------------------

When this repo was created, it was based off the upstream master branch. This branch was pushed as the upstream/master branch in the current repo.

To pull new changes from the upstream master branch, add the upstream remote:
```
git remote add upstream https://github.com/matrix-org/synapse.git
```

Make sure you're switched to the upstream/master branch and then pull in changes from the upstream remote:
```
git checkout upstream/master
git pull upstream master
```

Now merge the upstream/master branch into master:
```
git checkout master
git merge upstream/master
```
