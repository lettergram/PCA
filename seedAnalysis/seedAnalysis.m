function problem(f)
    file = '/Users/austin/Documents/Courses/cs498/hw8/seeds_dataset.csv';
    x = load(file);
    
    figure(1)
    filename = 'seedRegComp.gif';
    for v = 1:6
        for p = v:7
            % Roughly Color each point with associated seed type
            c = linspace(70,141,210);

            % Plot the first vs second principal component
            scatter(x(:,p), x(:,v), [], c, 'filled');
            t = strcat('component #', int2str(v), ' vs component #', int2str(p));
            title(t,'FontSize',14);
            ylabel(strcat('component #', int2str(v)),'FontSize',14);
            xlabel(strcat('component #', int2str(p)),'FontSize',14);
            axis([-25 25 -25 25]);

            drawnow
            frame = getframe(1);
            im = frame2im(frame);
            [imind,cm] = rgb2ind(im,256);
            if v == 1;
              imwrite(imind,cm,filename,'gif', 'Loopcount',inf);
            else
              imwrite(imind,cm,filename,'gif','WriteMode','append');
            end
        end
    end
    
    filename = 'seedPCAComp.gif'
    
    for v = 1:15
        % Run PCA on the matrix, determine only 2 top principal components 
        W = PCA(x, v, v+2);

        % Roughly Color each point with associated seed type
        c = linspace(70,141,210);

        % Plot the first vs second principal component
        scatter(W(:,1), W(:,2), [], c, 'filled');
        t = strcat('component #', int2str(v), ' vs component #', int2str(v+1));
        title(t,'FontSize',14);
        ylabel(strcat('component #', int2str(v)),'FontSize',14);
        xlabel(strcat('component #', int2str(v+1)),'FontSize',14);
        axis([-30 5 -5 5]);
        
        drawnow
        frame = getframe(1);
        im = frame2im(frame);
        [imind,cm] = rgb2ind(im,256);
        if v == 1;
          imwrite(imind,cm,filename,'gif', 'Loopcount',inf);
        else
          imwrite(imind,cm,filename,'gif','WriteMode','append');
        end
    end

    
    
    % SVD matrix 
    [U,S,V] = svd(x * transpose(x));
    
    % An eigenvalue is the diagonal matrix of S off the SVD component
    eV = diag(sqrt(S));
    
    % Plot the eigenvalues against eachother
    scatter(eV, eV, 'filled');
    
    % Plot only the top 10 sorted eigenvalue
    scatter(linspace(1,10,10), eV(1:10), 'filled')
    
end

% Find Weight for PCA
function W = PCA(matrix, s, e)
    [U,S,V] = svd(matrix * transpose(matrix));
    W = U * sqrt(S);
    W = W(:,s:e);
end