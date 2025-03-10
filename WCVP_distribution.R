library(rWCVP)

#load WCVP data

if (!require(rWCVPdata)) {
  install.packages("rWCVPdata",
    repos = c(
      "https://matildabrown.github.io/drat",
      "https://cloud.r-project.org"
    )
  )
}

names <- rWCVPdata::wcvp_names
distributions <- rWCVPdata::wcvp_distributions

x=read.table('~/Downloads/test.txt')
#Get distribution and plot for one species

for (i in 1:length(x$V1)) {
  result <- tryCatch({
    distribution <- wcvp_distribution(paste(x$V1[i],x$V2[i],sep=' '), taxon_rank="species")
  }, error = function(err) {
	print(paste(x$V1[i],x$V2[i],sep=' '))
    return(NULL)
  })

  # Code to execute if no error occurred
  if (!is.null(result)) {
  	pdf_file <- paste(x$V1[i],'_',x$V2[i],'.distr.pdf',sep='')
    pdf(pdf_file)
    #!!!Using print is critical to save to pdf in a for loop
    print(wcvp_distribution_map(distribution, crop_map=TRUE))
    #Sys.sleep(time = 2)
    dev.off()
  }
}