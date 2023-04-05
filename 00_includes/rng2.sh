nummer="$(((RANDOM % 10 ) +1))"
if [ $nummer -gt 5 ]
        then echo $nummer >> $HOME/techgrounds/rng2.txt
        else echo "Getal is 5 of lager" >> $HOME/techgrounds/rng2.txt
fi

