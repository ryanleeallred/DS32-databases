select_all = 'SELECT * from charactercreator_character;'

select_4_characters = '''SELECT character_id,name, hp
FROM charactercreator_character  
WHERE character_id>10 AND character_id <15;'''


right_mage_join = '''SELECT name, has_pet
FROM charactercreator_character 
LEFT JOIN charactercreator_mage
ON charactercreator_mage.character_ptr_id = charactercreator_character.character_id;'''