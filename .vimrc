" Basic Vim settings
set number                          " Show line numbers
set expandtab                       " Convert tabs to spaces
set tabstop=4                       " Set the number of spaces that a <Tab> counts for
set shiftwidth=4                    " Set the number of spaces used for each indentation level
set backspace=indent,eol,start      " Make the backspace key behave more intuitively
syntax on                           " Enable syntax highlighting
filetype plugin indent on           " Enable file type detection, plugins, and indenting
set hlsearch                        " Highlight search results
set incsearch                       " Incremental search
set showmatch                       " Show matching brackets
set mouse=a                         " Enable mouse support
set ruler                           " Display a ruler

" Initialize vim-plug
call plug#begin('~/.vim/plugged')

" Add plugins
Plug 'scrooloose/nerdtree'                " File tree explorer
Plug 'dense-analysis/ale'                 " Asynchronous Lint Engine
Plug 'nvie/vim-flake8'                    " Flake8 support
Plug 'fisadev/vim-pydocstyle'             " PEP257 compliance
Plug 'hynek/vim-python-pep8-indent'       " PEP8 indentation
Plug 'vim-syntastic/syntastic'            " Syntax checking

" End vim-plug block
call plug#end()

" NERDTree settings
map <C-n> :NERDTreeToggle<CR>       " Toggle NERDTree with Ctrl+n

" ALE settings
let g:ale_linters = {'python': ['flake8']}
let g:ale_python_flake8_options = '--max-line-length=79' " Follow PEP8 79 char line length

" Syntastic settings
let g:syntastic_python_checkers = ['flake8']
let g:syntastic_python_flake8_args = '--max-line-length=79' " Follow PEP8 79 char line length

" Autopep8 formatting
autocmd FileType python nnoremap <leader>f :call Autopep8()<CR>

function! Autopep8()
    let l:save = winsaveview()
    %!autopep8 - --max-line-length=79
    call winrestview(l:save)
endfunction

