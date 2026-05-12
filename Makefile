MODE = None
NAME = v46
all:
ifneq ($(NAME), v46)
	@(find . -type f -name "*" -print0 | xargs -0 sed -i'' -e "s/v46/$(NAME)/g")
	@(mv v46/v46.tex v46/$(NAME).tex)
	@(mv v46 $(NAME))
endif
	$(MAKE) -C $(NAME) MODE=$(MODE)
	cp $(NAME)/build/tex/$(NAME).pdf $(NAME)_rosenbaum_hikade.pdf

plots:
	$(MAKE) -C $(NAME) plot

clean:
	$(MAKE) -C $(NAME) clean

.PHONY: all clean
