-- file: format-authors.lua
local function squash_author(institutes)
	return function(author)
		local name = setmetatable(author.name, {})
		local institute = institutes[tonumber(author.institute[1])]
		return pandoc.MetaInlines(
			pandoc.List(name)
				.. pandoc.List({ pandoc.LineBreak() })
				.. pandoc.List(institute.name)
				.. pandoc.List({ pandoc.LineBreak() })
				.. author.email
		)
	end
end

function Meta(m)
	m.author = m.author:map(squash_author(m.institute))
	return m
end
