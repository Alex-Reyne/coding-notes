
- install conda pkg

```sh
# check conda version
conda -V # conda 4.11.0


# Create an environment
# will create a new environment named /envs/myDjangoEnv
conda create --name myDjangoEnv django
conda create --name myDjangoEnv python=3.7 # for specific python version

# for conda 4.6+
conda activate myDjangoEnv
conda deactivate

# for conda <4.6 & mac/linux, have to use 'source'
source activate myDjangoEnv
source deactivate myDjangoEnv

# lists all environments
conda info --envs

conda install django
  # currently 2.2.5




```


