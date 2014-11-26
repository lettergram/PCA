function x = problem(f)
    file = 'f.mat';
    x = load(file);
    s = 50;
    d = x.d;

    PCA(d, s);
    pcaGif(d, s);
end

% Find Weight for PCA and create GIF %
function pcaGif(matrix, s)
    [U,S,V] = svd(matrix * transpose(matrix));
    W = U * sqrt(S);
    W = W(:,1:s);
    
    figure(1);
    filename = 'PCA.gif';
    
    for i = 1:s
        imagesc(reshape(W(:,i),28,28))
        title(['Principal Component #' num2str(i)])
        drawnow
        frame = getframe(1);
        im = frame2im(frame);
        [imind,cm] = rgb2ind(im,256);
        if i == 1;
          imwrite(imind,cm,filename,'gif', 'Loopcount',inf);
        else
          imwrite(imind,cm,filename,'gif','WriteMode','append');
        end
    end
end

% Find Weight for PCA %
function W = PCA(matrix, s)
    [U,S,V] = svd(matrix * transpose(matrix));
    W = U * sqrt(S);
    W = W(:,1:s);
    for i = 1:s
        subplot(6,6,i)
        imagesc(reshape(W(:,i),28,28))
        ylabel(['PCA #' num2str(i)])
        title('PCA')
    end
end
