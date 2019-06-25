def commonfind(a,b):
    for item in a:
        if item in b:
            return True


akatsuki=['pain','konan','zetsu','obito','madara','itachi','kisame','sasori','deidara','hidan','kakazu']
uchiha=['itachi','obito','madara','sasuke','shisui']
print(commonfind(akatsuki,uchiha))
