apl_query = """
select * from public.apple_data 
	where "Primary_Genre" in 
		('Games','Music','Health & Fitness');
"""

and_query = """
select * from public.android_data 
	where "Category" in 
		('Action',
		'Adventure',
		'Arcade',
		'Board',
		'Card',
		'Casino',
		'Casual',
		'Educational',
		'Health & Fitness',
		'Music',
		'Music & Audio',
		'Puzzle',
		'Racing',
		'Role Playing',
		'Simulation',
		'Sports',
		'Strategy',
		'Trivia',
		'Word');
"""

and_query_cleaned = """with android_subset as (
select * from public.android_data 
	where "Category" in 
		('Action',
		'Adventure',
		'Arcade',
		'Board',
		'Card',
		'Casino',
		'Casual',
		'Educational',
		'Health & Fitness',
		'Music',
		'Music & Audio',
		'Puzzle',
		'Racing',
		'Role Playing',
		'Simulation',
		'Sports',
		'Strategy',
		'Trivia',
		'Word')
),
android_cleaned as (
select 
	"App_Name" as "name",
	"Released" as release_date,
	right("Released",4) as release_year,
	"Size" as filesize,
	case 
		when "Category" = 'Music & Audio' then 'Music'
		when "Category" = 'Health & Fitness' then 'Health & Fitness'
		else 'Games'
	end as genre,
	"Rating" as rating,
	"Rating_Count" as rating_amt,
	'android' as platform
from android_subset 
where "Released" is not null
)
select * from android_cleaned;
"""

apl_cleaned_query = """with apple_subset as (
select * from public.apple_data 
	where "Primary_Genre" in 
		('Games','Music','Health & Fitness')
),
apple_cleaned as (
select 
	"App_Name" as "name",
	"Released" as release_date,
	left("Released",4) as release_year,
	"Size_Bytes" as filesize,
	"Primary_Genre" as genre,
	"Average_User_Rating" as rating,
	"Reviews" as rating_amt,
	'apple' as platform
from apple_subset
)
select * from apple_cleaned;"""