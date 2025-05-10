! (register-module! ../new-project)
! (import! &self new-project:data)

(= (extractGenere $genre $space)
     (match $space ($id $title $genre $actor $year $dir $des) ($id $title $genre $actor $year $dir $des)))

(= (extractMovie $))    

; ; lets assume that we have maximum of 4 filters

! (println!(extractGenere $genre &self))

;! (get-metatype "Akshat")