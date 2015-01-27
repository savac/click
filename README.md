#### Vowpal Wabbit guide

##### Install
sudo apt-get install libboost-all-dev<br />
./configure --with-boost-libdir=/usr/lib/x86_64-linux-gnu​ (needs to be passed the location on Boost)<br />
make<br />
sudo make install (this fails)<br />
make test (also fails)<br />
vw -- version<br />

Command line
============

VW options:
  --random_seed arg                     seed random number generator
  --ring_size arg                       size of example ring

Update options:
  -l [ --learning_rate ] arg            Set learning rate
  --power_t arg                         t power value
  --decay_learning_rate arg             Set Decay factor for learning_rate 
                                        between passes
  --initial_t arg                       initial t value
  --feature_mask arg                    Use existing regressor to determine 
                                        which parameters may be updated.  If no
                                        initial_regressor given, also used for 
                                        initial weights.

Weight options:
  -i [ --initial_regressor ] arg        Initial regressor(s)
  --initial_weight arg                  Set all weights to an initial value of 
                                        1.
  --random_weights arg                  make initial weights random
  --input_feature_regularizer arg       Per feature regularization input file

Parallelization options:
  --span_server arg                     Location of server for setting up 
                                        spanning tree
  --unique_id arg                       unique id used for cluster parallel 
                                        jobs
  --total arg                           total number of nodes used in cluster 
                                        parallel job
  --node arg                            node number in cluster parallel job

Diagnostic options:
  --version                             Version information
  -a [ --audit ]                        print weights of features
  -P [ --progress ] arg                 Progress update frequency. int: 
                                        additive, float: multiplicative
  --quiet                               Don't output disgnostics and progress 
                                        updates
  -h [ --help ]                         Look here: http://hunch.net/~vw/ and 
                                        click on Tutorial.

Feature options:
  --hash arg                            how to hash the features. Available 
                                        options: strings, all
  --ignore arg                          ignore namespaces beginning with 
                                        character <arg>
  --keep arg                            keep namespaces beginning with 
                                        character <arg>
  -b [ --bit_precision ] arg            number of bits in the feature table
  --noconstant                          Don't add a constant feature
  -C [ --constant ] arg                 Set initial value of constant
  --ngram arg                           Generate N grams. To generate N grams 
                                        for a single namespace 'foo', arg 
                                        should be fN.
  --skips arg                           Generate skips in N grams. This in 
                                        conjunction with the ngram tag can be 
                                        used to generate generalized 
                                        n-skip-k-gram. To generate n-skips for 
                                        a single namespace 'foo', arg should be
                                        fN.
  --feature_limit arg                   limit to N features. To apply to a 
                                        single namespace 'foo', arg should be 
                                        fN
  --affix arg                           generate prefixes/suffixes of features;
                                        argument '+2a,-3b,+1' means generate 
                                        2-char prefixes for namespace a, 3-char
                                        suffixes for b and 1 char prefixes for 
                                        default namespace
  --spelling arg                        compute spelling features for a give 
                                        namespace (use '_' for default 
                                        namespace)
  --dictionary arg                      read a dictionary for additional 
                                        features (arg either 'x:file' or just 
                                        'file')
  -q [ --quadratic ] arg                Create and use quadratic features
  --q: arg                              : corresponds to a wildcard for all 
                                        printable characters
  --cubic arg                           Create and use cubic features

Example options:
  -t [ --testonly ]                     Ignore label information and just test
  --holdout_off                         no holdout data in multiple passes
  --holdout_period arg                  holdout period for test only, default 
                                        10
  --holdout_after arg                   holdout after n training examples, 
                                        default off (disables holdout_period)
  --early_terminate arg                 Specify the number of passes tolerated 
                                        when holdout loss doesn't decrease 
                                        before early termination, default is 3
  --passes arg                          Number of Training Passes
  --initial_pass_length arg             initial number of examples per pass
  --examples arg                        number of examples to parse
  --min_prediction arg                  Smallest prediction to output
  --max_prediction arg                  Largest prediction to output
  --sort_features                       turn this on to disregard order in 
                                        which features have been defined. This 
                                        will lead to smaller cache sizes
  --loss_function arg (=squared)        Specify the loss function to be used, 
                                        uses squared by default. Currently 
                                        available ones are squared, classic, 
                                        hinge, logistic and quantile.
  --quantile_tau arg (=0.5)             Parameter \tau associated with Quantile
                                        loss. Defaults to 0.5
  --l1 arg                              l_1 lambda
  --l2 arg                              l_2 lambda

Output model:
  -f [ --final_regressor ] arg          Final regressor
  --readable_model arg                  Output human-readable final regressor 
                                        with numeric features
  --invert_hash arg                     Output human-readable final regressor 
                                        with feature names.  Computationally 
                                        expensive.
  --save_resume                         save extra state so learning can be 
                                        resumed later with new data
  --save_per_pass                       Save the model after every pass over 
                                        data
  --output_feature_regularizer_binary arg
                                        Per feature regularization output file
  --output_feature_regularizer_text arg Per feature regularization output file,
                                        in text

Reduction options, use [option] --help for more info:

  --bootstrap arg                       k-way bootstrap by online importance 
                                        resampling

  --search arg                          Use learning to search, 
                                        argument=maximum action id or 0 for LDF

  --cbify arg                           Convert multiclass on <k> classes into 
                                        a contextual bandit problem

  --cb arg                              Use contextual bandit learning with <k>
                                        costs

  --csoaa_ldf arg                       Use one-against-all multiclass learning
                                        with label dependent features.  Specify
                                        singleline or multiline.

  --wap_ldf arg                         Use weighted all-pairs multiclass 
                                        learning with label dependent features.
                                          Specify singleline or multiline.

  --csoaa arg                           One-against-all multiclass with <k> 
                                        costs

  --log_multi arg                       Use online tree for multiclass

  --ect arg                             Error correcting tournament with <k> 
                                        labels

  --oaa arg                             One-against-all multiclass with <k> 
                                        labels

  --top arg                             top k recommendation

  --binary                              report loss as binary classification on
                                        -1,1

  --link arg (=identity)                Specify the link function: identity, 
                                        logistic or glf1

  --stage_poly                          use stagewise polynomial feature 
                                        learning

  --lrq arg                             use low rank quadratic features

  --autolink arg                        create link function with polynomial d

  --new_mf arg                          rank for reduction-based matrix 
                                        factorization

  --nn arg                              Sigmoidal feedforward network with <k> 
                                        hidden units

  --active                              enable active learning

  --bfgs                                use bfgs optimization

  --conjugate_gradient                  use conjugate gradient based 
                                        optimization

  --lda arg                             Run lda with <int> topics

  --noop                                do no learning

  --print                               print examples

  --rank arg                            rank for matrix factorization.

  --sendto arg                          send examples to <host>

  --ftrl                                Follow the Regularized Leader

  --ksvm                                kernel svm

Gradient Descent options:
  --sgd                                 use regular stochastic gradient descent
                                        update.
  --adaptive                            use adaptive, individual learning 
                                        rates.
  --invariant                           use safe/importance aware updates.
  --normalized                          use per feature normalized updates
  --exact_adaptive_norm                 use current default invariant 
                                        normalized adaptive update rule

Output options:
  -p [ --predictions ] arg              File to output predictions to
  -r [ --raw_predictions ] arg          File to output unnormalized predictions
                                        to

Input options:
  -d [ --data ] arg                     Example Set
  --daemon                              persistent daemon mode on port 26542
  --port arg                            port to listen on; use 0 to pick unused
                                        port
  --num_children arg                    number of children for persistent 
                                        daemon mode
  --pid_file arg                        Write pid file in persistent daemon 
                                        mode
  --port_file arg                       Write port used in persistent daemon 
                                        mode
  -c [ --cache ]                        Use a cache.  The default is 
                                        <data>.cache
  --cache_file arg                      The location(s) of cache_file.
  -k [ --kill_cache ]                   do not reuse existing cache: create a 
                                        new one always
  --compressed                          use gzip format whenever possible. If a
                                        cache file is being created, this 
                                        option creates a compressed cache file.
                                        A mixture of raw-text & compressed 
                                        inputs are supported with 
                                        autodetection.
  --no_stdin                            do not default to reading from stdin


