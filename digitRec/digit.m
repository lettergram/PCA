function x = problem(f)
file = '/Users/austin/program/algorithms/pca/digitRec/digits.mat';
x = load(file);
s = 36;
d = x.d;

W = PCA(d, s);
NMF(d, s);
end

% Find Weight for PCA%
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