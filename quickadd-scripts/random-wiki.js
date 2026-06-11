module.exports = async (params) => {
    const { TFolder, TFile, Notice } = require('obsidian');
    
    const wikiFolder = app.vault.getAbstractFileByPath("wiki");
    if (!wikiFolder || !(wikiFolder instanceof TFolder)) {
        new Notice("找不到 wiki 文件夹");
        return;
    }
    
    // 递归收集 wiki 目录下所有 md 文件
    const collectFiles = (folder) => {
        let files = [];
        for (const child of folder.children) {
            if (child instanceof TFile && child.extension === "md") {
                files.push(child);
            } else if (child instanceof TFolder) {
                files = files.concat(collectFiles(child));
            }
        }
        return files;
    };
    
    const files = collectFiles(wikiFolder);
    if (files.length === 0) {
        new Notice("wiki 目录下没有 markdown 文件");
        return;
    }
    
    const randomFile = files[Math.floor(Math.random() * files.length)];
    await app.workspace.openLinkText(randomFile.path, "", false);
    new Notice(`🎲 ${randomFile.name}`);
};
