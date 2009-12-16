def receive_new_code:
        $body = pg_escape_string ( $_POST['code']['body'] );
        $title = pg_escape_string ( $_POST['code']['title'] );
        $tags = $_POST['code']['tags'];

        # login validation
        # body, tags validatian

        # take body from $_POST['code']['body']
        # put code to db, put tags to db by running separate functions
        # get code_id in the db such that we can redirect the user to his
        # question at /index.py?code_id=777
            # ? pass the code_in in GET like /index.py?code_sent&code_id
        # else put him to /index.py?unsuccessful

receive_new_question (); 
